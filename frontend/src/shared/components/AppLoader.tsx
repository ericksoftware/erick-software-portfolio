import { motion } from 'motion/react'

export function AppLoader() {
  return (
    <main
      className="app-state"
      aria-busy="true"
      aria-live="polite"
    >
      <motion.div
        className="app-loader"
        initial={{ opacity: 0, scale: 0.92 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{
          duration: 0.4,
          ease: 'easeOut',
        }}
      >
        <div className="app-loader__mark">
          ER
        </div>

        <p>Cargando experiencia digital</p>

        <div
          className="app-loader__line"
          aria-hidden="true"
        >
          <motion.span
            initial={{ scaleX: 0 }}
            animate={{ scaleX: 1 }}
            transition={{
              duration: 1.2,
              repeat: Infinity,
              repeatType: 'reverse',
              ease: 'easeInOut',
            }}
          />
        </div>
      </motion.div>
    </main>
  )
}